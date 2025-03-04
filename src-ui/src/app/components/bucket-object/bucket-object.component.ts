import {Component, Input, signal} from '@angular/core';
import {BucketObject} from '../../interface/bucketObject';
import {DatePipe, NgForOf} from '@angular/common';
import {FormsModule} from '@angular/forms';
import {FilterObjPipe} from '../../pipes/filter-obj.pipe';

@Component({
  selector: 'app-bucket-object',
  imports: [
    NgForOf,
    DatePipe,
    FormsModule, FilterObjPipe,
  ],
  templateUrl: './bucket-object.component.html',
  styleUrl: './bucket-object.component.css'
})
export class BucketObjectComponent {
 searchTerm !: string;
  @Input() bucObjs!: BucketObject[];

}
