import { Component, NgZone, OnDestroy, OnInit, ViewEncapsulation } from '@angular/core';
import { User } from 'firebase';
import {} from 'googlemaps';
import { AngularFirestore } from '@angular/fire/firestore';
import { Observable, Subscription } from 'rxjs';
import { LoginService } from '../../services/login.service';
import * as firebase from 'firebase/app';
import { CursorError } from '@angular/compiler/src/ml_parser/lexer';

@Component({
  selector: 'app-map-page',
  templateUrl: './map-page.component.html',
  styleUrls: ['./map-page.component.scss'],
  encapsulation: ViewEncapsulation.None
})
export class MapPageComponent implements OnInit, OnDestroy {
  
  locationUpdateDoc = '';
  locationUpdatesCollection = 'location-updates';
  driverId = '';

  authUser: User;
  authUserSub: Subscription;
  
  showMapPill: boolean;
  mapLoaded: boolean;
  map: google.maps.Map;
  center: google.maps.LatLngLiteral;

  time: string = '';
  distance: string = '';

  source: google.maps.LatLngLiteral;
  destination: google.maps.LatLngLiteral;

  sourcePin: google.maps.Marker;
  destinationPin: google.maps.Marker;
  sourcePoint: google.maps.Marker;
  SignPin: google.maps.Marker;
  
  locationWatchId: number;
  locSimulationInterval: any;
  destinationSet: boolean;
  latLngs: any[];
  locationUpdateObj: any;

  options: google.maps.MapOptions = {
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    scrollwheel: true,
    disableDefaultUI: true,
    disableDoubleClickZoom: true,
    zoom: 12
  }

  ds: google.maps.DirectionsService;
  dr: google.maps.DirectionsRenderer;

  placesText: string;
  togglePlacesSearch: boolean = false;

  constructor(
    private firestore: AngularFirestore,
    private loginService: LoginService,
    private ngZone: NgZone) {}

  async ngOnInit() {

    this.authUserSub = this.loginService.getLoggedInUser().subscribe((user: User) => {
      this.authUser = user;
    });
    this.driverId = this.authUser.uid;

    //var rand = Math.random() * 100000000000000
    this.locationUpdateDoc = this.authUser.displayName;
    this.firestore
        .collection(this.locationUpdatesCollection)
        .doc(this.locationUpdateDoc)
        .set({
          route: "",
          source: {
            location: {
              lat: "",
              lng: ""
            },
            uid: ""
          },
          destination: {
            location: {
              lat: "",
              lng: ""
            },
            uid: ""
          }
        }, { merge: true });


    this.ds = new google.maps.DirectionsService();
    this.dr = new google.maps.DirectionsRenderer({
      map: null,
      suppressMarkers: true
    });

    // get initial current position
    navigator.geolocation.getCurrentPosition(position => {

      this.center = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };

      this.source = this.center;

      this.firestore
        .collection(this.locationUpdatesCollection)
        .doc(this.locationUpdateDoc)
        .set({
          source: {
            location: {
              lat: this.source.lat,
              lng: this.source.lng
            },
            uid: this.authUser.uid
          }
        }, { merge: true });
      

      // initialize the map container
      this.map = new google.maps.Map(document.getElementById('map-canvas'), {
        ...this.options,
        center: this.source
      });

      this.map.addListener('tilesloaded', () => {
        this.ngZone.run(() => {
          this.mapLoaded = true;
        });
      });

      this.sourcePin = new google.maps.Marker({
        position: this.source,
        icon: {
          url: './assets/imgs/car_pin.svg',
          anchor: new google.maps.Point(18,30),
          origin: new google.maps.Point(0,0),
          scaledSize: new google.maps.Size(40, 40)
        },
        map: this.map
      });

      this.map.addListener("click", (event: any) => {
        this.showMapPill = false;
      });
    });

    // watch position as it changes
    this.locationWatchId = navigator.geolocation.watchPosition(
      (position) => {
  
        // if it's the driver user that's logged in,
        // then update its location as he / she moves
        this.source = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
          };
  
          if (this.sourcePin) {
            this.sourcePin.setPosition(this.source);
          }
          
          this.firestore
          .collection(this.locationUpdatesCollection)
          .doc(this.locationUpdateDoc)
          .set({
            source: {
              location: {
                lat: this.source.lat,
                lng: this.source.lng
              },
              uid: this.authUser.uid
            }
          }, { merge: true });
        
      },
      (error) => {
        // handle error of watch position
    });

    // listen for updates on the locationUpdateDoc
    this.firestore.collection(this.locationUpdatesCollection)
    .doc(this.locationUpdateDoc).
    ref.onSnapshot(snapshot => {
      let updatedSourceLocation = snapshot.data();

      // if this is the package receiver user...
      if (updatedSourceLocation.destination &&
        updatedSourceLocation.destination.uid === this.authUser.uid) {
        
        this.dr.setOptions({
          suppressPolylines: false,
          map: this.map
        });

        // set the route information once initially
        if (this.dr && updatedSourceLocation.route && !this.destinationSet) {
          let response = JSON.parse(updatedSourceLocation.route)
          this.dr.setDirections(response);

          this.ngZone.run(() => {
            let distanceInfo = response.routes[0].legs[0];
            this.distance = distanceInfo.distance.text;
            this.time = distanceInfo.duration.text;
          });

          this.destinationSet = !this.destinationSet;
        }

        // check that the updated source info (the youps driver location)
        // then update the source pin on the receiving user side
        if (updatedSourceLocation.source) {
          this.source = {
            lat: updatedSourceLocation.source.location.lat,
            lng: updatedSourceLocation.source.location.lng
          };
    
          this.setupSourcePin();
        }
      }
    });    
  }


  setupSourcePin() {
    if (!this.destinationPin) {
      // adding a marker
      this.destinationPin = new google.maps.Marker({
        position: this.destination,
        icon: {
          url: './assets/imgs/pin.svg',
          anchor: new google.maps.Point(18,30),
          origin: new google.maps.Point(0,0),
          scaledSize: new google.maps.Size(40, 40)
        },
        animation: google.maps.Animation.DROP,
        map: this.map
      });

      this.destinationPin.addListener("click", (event: any) => {
        this.showMapPill = true;
        this.onCenterMap();
      });
    }
    else {
      this.destinationPin.setPosition(this.destination);
    }
  }

  setRoutePolyline() {
    let latDire = 9.0;
    let lngDire = 89.0;
    let currentLat = 9.0;
    let currentLng = 89.0;

    let request = {
      origin: this.source,
      destination: this.destination,
      travelMode: google.maps.TravelMode.DRIVING
    };

    this.ds.route(request, async (response: any, status: any) => {
      this.dr.setOptions({
        suppressPolylines: false,
        map: this.map
      });

      if (status == google.maps.DirectionsStatus.OK) {
        this.dr.setDirections(response);

       let step: any = response.routes[0].overview_path;
       step.forEach(async (stepPoint) => {
         latDire = stepPoint.lat();
         lngDire = stepPoint.lng();
        
         this.firestore.collection(this.locationUpdatesCollection)
         .doc(this.locationUpdateDoc).
         ref.onSnapshot(snapshot => {
           let updatedSourceLocation = snapshot.data();
           currentLat = updatedSourceLocation.source.location.lat;
           currentLng = updatedSourceLocation.source.location.lng;
         });

        (await firebase.firestore().collection('coordinate100').get()).forEach(doc =>{
          const docu = doc.data();
            let laTt = parseFloat(docu.lat);
            let lnGg = parseFloat(docu.lng);
            const myLatLng = { lat: 8.9, lng: 81.2};
            if ((currentLat <= laTt && laTt <= latDire) || (latDire <= laTt && laTt <= currentLat) || 
                (currentLng <= lnGg && lnGg <= lngDire) || (lngDire <= lnGg && lnGg <= currentLng)){
              if(docu.sign == "stop"){
              myLatLng.lat=laTt;
              myLatLng.lng=lnGg;
              new google.maps.Marker({
                position: myLatLng,
                icon: {
                  url: './assets/imgs/stop.svg',
                  anchor: new google.maps.Point(18,30),
                  origin: new google.maps.Point(0,0),
                  scaledSize: new google.maps.Size(20, 20)
                  },
                map: this.map
                });
              }
              else if (docu.sign == "zebra"){
                myLatLng.lat=laTt;
                myLatLng.lng=lnGg;
                new google.maps.Marker({
                  position: myLatLng,
                  icon: {
                    url: './assets/imgs/zebra.svg',
                    anchor: new google.maps.Point(18,30),
                    origin: new google.maps.Point(0,0),
                    scaledSize: new google.maps.Size(20, 20)
                  },
                  map: this.map
                });
              }
          }
        });      
      });  

        if (this.authUser.uid) {
          
          this.latLngs = [];
          let step: any = response.routes[0].legs[0].steps[0];
          step.lat_lngs.forEach((stepPoint) => {
            this.latLngs.push({
              lat: stepPoint.lat(),
              lng: stepPoint.lng()
            });
          });

          this.firestore
            .collection(this.locationUpdatesCollection)
            .doc(this.locationUpdateDoc)
            .set({
              route: JSON.stringify(response),
              destination: {
                location: {
                  lat: this.destination.lat,
                  lng: this.destination.lng
                },
                uid: this.authUser.uid
              }
            }, { merge: true });
            let count = 0;
            this.locSimulationInterval = setInterval(() => {
              if (count < this.latLngs.length) {
                let currentPos = this.latLngs[count];
                this.firestore
                .collection(this.locationUpdatesCollection)
                .doc(this.locationUpdateDoc)
                .set({
                  source: {
                    location: {
                      lat: currentPos.lat,
                      lng: currentPos.lng
                    },
                    uid: this.authUser.uid
                  }
                }, { merge: true });
                count++;

                this.source = currentPos;
                this.setupSourcePin();
              }
            }, 1000);            
        }

        this.ngZone.run(() => {
          let distanceInfo = response.routes[0].legs[0];
          this.distance = distanceInfo.distance.text;
          this.time = distanceInfo.duration.text;
        });
      }
    })
  }

  handleAddressChange(event: any) {
    const lat = event.geometry.location.lat();
    const lng = event.geometry.location.lng();

    this.destination = {
      lat: lat,
      lng: lng
    };

    this.setupSourcePin();
    this.setRoutePolyline();
  }

  onCenterMap() {
    this.map.panTo(this.source);
  }

  onLogout() {
    this.loginService.logout();
  }

  clearPlacesField() {
    this.placesText = "";
  }

  toggleSearch() {
    this.togglePlacesSearch = !this.togglePlacesSearch;
  }

  ngOnDestroy() {
    navigator.geolocation.clearWatch(this.locationWatchId);
    clearInterval(this.locSimulationInterval);
  }
}
