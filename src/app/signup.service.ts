import { Injectable } from '@angular/core';

import { Observable, of } from 'rxjs';

import { User } from './hero';
import { HEROES } from './mock-heroes';
import { MessageService } from './message.service';

import { HttpClient, HttpHeaders } from '@angular/common/http';
//import { Http, Headers, Response, RequestOptions, RequestMethod } from '@angular/common/http';

import { catchError, map, tap } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class SignupService {
  private heroesUrl = 'https://reqres.in';  // URL to web api

  constructor(
    private http: HttpClient,
    private messageService: MessageService) { }

  /** Log a HeroService message with the MessageService */
  private log(message: string) {
    this.messageService.add(`HeroService: ${message}`);
  }

  /**
 * Handle Http operation that failed.
 * Let the app continue.
 * @param operation - name of the operation that failed
 * @param result - optional value to return as the observable result
 */
  private handleError<T>(operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  /** GET heroes from the server */
  /** GET heroes from the server */
  // validateUser(hero: User): Observable<User[]> {
  //   const url = `${this.heroesUrl}/api/register`;
  //   return this.http.post<User[]>(url,hero,this.httpOptions)
  //     .pipe(
  //       tap((newUser: User)=> this.log('post heroes')),
  //       catchError(this.handleError<User[]>('validateUser'))
  //     );
  // }

  register(user: User) {
    console.log(user)
    const httpOptions = {
      headers: new HttpHeaders({
        'Content-Type': 'application/json',
        // 'Authorization': 'my-auth-token'
      })
    };
    const url = `${this.heroesUrl}/api/register`;
    console.log("service", url)
    return this.http.post(url, user, httpOptions)
    .subscribe(response => {
        console.log(response);
        return response;
    }, err => {
        throw err;
    });

  }
}
