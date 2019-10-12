import { NgModule }       from '@angular/core';
import { BrowserModule }  from '@angular/platform-browser';
import { FormsModule }    from '@angular/forms';

import { AppComponent }         from './app.component';
import { DashboardComponent }   from './dashboard/dashboard.component';
import { HeroDetailComponent }  from './hero-detail/hero-detail.component';
import { HeroesComponent }      from './heroes/heroes.component';
import { MessagesComponent }    from './messages/messages.component';

import { ReactiveFormsModule } from '@angular/forms';

import { AppRoutingModule }     from './app-routing.module';
import { HttpClientModule , HTTP_INTERCEPTORS }    from '@angular/common/http';

// import { HttpClientInMemoryWebApiModule } from 'angular-in-memory-web-api';
// import { InMemoryDataService }  from './in-memory-data.service';
import { SignupComponent } from './signup/signup.component';
import { LoginComponent } from './login/login.component';
import { JwtInterceptor } from './helpers/jwt.interceptor';
import { ErrorInterceptor } from './helpers/error.interceptor';
import { AlertComponent } from './alert/alert.component';
import { TodoComponent } from './todo/todo.component'

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    AppRoutingModule,
    HttpClientModule,
    // HttpClientInMemoryWebApiModule,
    HttpClientModule,
//     HttpClientInMemoryWebApiModule.forRoot(
//       InMemoryDataService, { dataEncapsulation: false }
// )

  ],
  providers: [
      { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
      { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },

      // provider used to create fake backend
      //fakeBackendProvider
  ],
  declarations: [
    AppComponent,
    DashboardComponent,
    HeroesComponent,
    HeroDetailComponent,
    MessagesComponent,
    SignupComponent,
    LoginComponent,
    AlertComponent,
    TodoComponent
  ],
  // providers: [
  //       { provide: HTTP_INTERCEPTORS, useClass: JwtInterceptor, multi: true },
  //       { provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true },
  //
  //
  //   ],
  bootstrap: [ AppComponent ]
})
export class AppModule { }
