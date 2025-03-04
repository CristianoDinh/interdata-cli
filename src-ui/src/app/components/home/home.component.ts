import {Component, inject} from '@angular/core';
import {BucketObject} from '../../interface/bucketObject';
import {ObjectService} from '../../services/object.service';
import {NgForOf} from '@angular/common';
import {BucketObjectComponent} from '../bucket-object/bucket-object.component';

@Component({
  selector: 'app-home',
  imports: [
    NgForOf,
    BucketObjectComponent
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  bucketObjectList: BucketObject[] = [];
  objectService: ObjectService = inject(ObjectService);

  constructor() {
    this.bucketObjectList = this.objectService.getAllBucketObjects();
  }


}
