import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { DashboardComponent }   from './dashboard/dashboard.component';
import { HeroesComponent }      from './heroes/heroes.component';
import { HeroDetailComponent }  from './hero-detail/hero-detail.component';
import { SignupComponent }  from './signup/signup.component';
import { LoginComponent } from './login/login.component';
import { AuthGuard } from './helpers/auth.guard';
const routes: Routes = [

  { path: '', redirectTo: '/heroes', pathMatch: 'full' , canActivate:
  [AuthGuard] },
  { path: 'dashboard', component: DashboardComponent },
  { path: 'detail/:id', component: HeroDetailComponent },
  { path: 'heroes', component: HeroesComponent, canActivate:
  [AuthGuard]},
  { path: 'signup', component: SignupComponent},
    { path: 'login', component: LoginComponent}
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
