import { Component, Input } from '@angular/core';
import {BucketObject} from '../../interface/bucketObject';
import {NgForOf} from '@angular/common';

@Component({
  selector: 'app-bucket-object',
  imports: [
    NgForOf
  ],
  templateUrl: './bucket-object.component.html',
  styleUrl: './bucket-object.component.css'
})
export class BucketObjectComponent {
  @Input() bucObjs!: BucketObject[];
}
