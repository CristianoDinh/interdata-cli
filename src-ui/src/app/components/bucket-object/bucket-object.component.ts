import { Component, Input } from '@angular/core';
import {BucketObject} from '../../interface/bucketObject';
import {DatePipe, NgForOf} from '@angular/common';

@Component({
  selector: 'app-bucket-object',
  imports: [
    NgForOf,
    DatePipe
  ],
  templateUrl: './bucket-object.component.html',
  styleUrl: './bucket-object.component.css'
})
export class BucketObjectComponent {
  @Input() bucObjs!: BucketObject[];
}
