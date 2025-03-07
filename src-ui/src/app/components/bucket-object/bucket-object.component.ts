import {Component, Input, signal} from '@angular/core';
import {NgForOf} from '@angular/common';
import {FormsModule} from '@angular/forms';
import {FilterObjPipe} from '../../pipes/filter-obj.pipe';
import {S3Bucket} from '../../interface/S3Bucket';
import {S3Object} from '../../interface/S3Object';

@Component({
  selector: 'app-bucket-object',
  imports: [
    NgForOf,
    FormsModule, FilterObjPipe,
  ],
  templateUrl: './bucket-object.component.html',
  styleUrl: './bucket-object.component.css'
})
export class BucketObjectComponent {
  @Input() search !: string;
  filter !: string;

  @Input() buckets !: S3Bucket[];
  @Input() bucObjs!: S3Object[];

}
