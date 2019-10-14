import { Injectable } from '@angular/core';
import { MessageService } from './message.service';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Todo } from './hero';

@Injectable({
  providedIn: 'root'
})
export class TodoService {
  private Url = 'http://127.0.0.1:8000/api/v1/todo/todolistcreate/';
  constructor(private http: HttpClient) { }

  getTodo(): Observable<Todo[]> {
    return this.http.get<Todo[]>(this.Url, )
      .pipe(map(response => {
        // store user details and jwt token in local storage to keep user logged in between page refreshes
        //localStorage.setItem('currentUser', JSON.stringify(user));
        //this.currentUserSubject.next(user);
        console.log(response)
        return response;
      }));

  }
  getTodo2(url?: string): Observable<Todo[]> {
    //const url = `${url}`;
    return this.http.get<Todo[]>(url, )
      .pipe(map(response => {
        // store user details and jwt token in local storage to keep user logged in between page refreshes
        //localStorage.setItem('currentUser', JSON.stringify(user));
        //this.currentUserSubject.next(user);
        console.log(response)
        return response;
      }));
    // .subscribe(response => {
    //   console.log(response);
    //   return response;
    // }, err => {
    //   throw err;
    // });
  }
}
