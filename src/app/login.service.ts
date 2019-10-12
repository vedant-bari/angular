import { Injectable } from '@angular/core';
import { MessageService } from './message.service';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { User, UserToken } from './hero';
@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private currentUserSubject: BehaviorSubject<any>;
  public currentUser: Observable<any>;

  constructor(private http: HttpClient) {
    this.currentUserSubject = new BehaviorSubject<UserToken>(JSON.parse(localStorage.getItem('currentUser')));
    this.currentUser = this.currentUserSubject.asObservable();
  }

  public get currentUserValue(): UserToken {
    return this.currentUserSubject.value;
  }

  // login(email, password) {
  //   return this.http.post<any>(`http://127.0.0.1:8000/rest-auth/login/`, { email, password })
  //     .subscribe(response => {
  //       console.log(response);
  //       return response;
  //     }, err => {
  //       throw err;
  //     });
                                                                                                                                                                                                      //                                                                                                                                                                          }

  login(email, password) {
    return this.http.post<any>(`http://127.0.0.1:8000/rest-auth/login/`, { email, password })
              .pipe(map(user => {
                         // store user details and jwt token in local storage to keep user logged in between page refreshes
                         localStorage.setItem('currentUser', JSON.stringify(user));
                         this.currentUserSubject.next(user);
                         return user;
                     }))
                // .subscribe(response => {
                //   console.log(response);
                //   return response;
                // }, err => {
                //   throw err;
                // });
  }

  logout() {
    // remove user from local storage and set current user to null
    localStorage.removeItem('currentUser');
    this.currentUserSubject.next(null);
  }
}
