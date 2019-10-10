import { Injectable } from '@angular/core';
import { MessageService } from './message.service';
import { BehaviorSubject, Observable } from 'rxjs';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { User } from './hero';
@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private currentUserSubject: BehaviorSubject<User>;
  public currentUser: Observable<User>;

  constructor(private http: HttpClient) {
    this.currentUserSubject = new BehaviorSubject<User>(JSON.parse(localStorage.getItem('currentUser')));
    this.currentUser = this.currentUserSubject.asObservable();
  }

  public get currentUserValue(): User {
    return this.currentUserSubject.value;
  }

  login(email, password) {
    return this.http.post<any>(`http://127.0.0.1:8000/rest-auth/login/`, { email, password })
      .subscribe(response => {
        console.log(response);
        return response;
      }, err => {
        throw err;
      });
  }

  logout() {
    // remove user from local storage and set current user to null
    localStorage.removeItem('currentUser');
    this.currentUserSubject.next(null);
  }
}
