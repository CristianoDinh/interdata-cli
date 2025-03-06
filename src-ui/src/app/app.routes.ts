import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import {TestAPIComponent} from './test-api/test-api.component';
import {NotFoundComponent} from './components/not-found/not-found.component';

export const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    title: 'HomePage'
  },
  {
    path: 'test',
    component: TestAPIComponent,
    title: 'Test Flask API'
  },
  {
    path: '**',
    component: NotFoundComponent,
    title: 'Page Not Found'
  }

];
