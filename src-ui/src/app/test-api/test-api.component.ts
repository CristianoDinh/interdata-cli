import {Component, inject, OnInit} from '@angular/core';
import {S3Service} from '../services/s3.service';
import {NgForOf, NgIf} from '@angular/common';

@Component({
  selector: 'app-test-api',
  imports: [
    NgIf,
    NgForOf
  ],
  templateUrl: './test-api.component.html',
  styleUrl: './test-api.component.css'
})
export class TestAPIComponent implements OnInit {
  //1. get Buckets
   buckets: any[] = [];
   s3 = inject(S3Service);

  ngOnInit() {
    this.s3.getBuckets().subscribe(data => {
      this.buckets = data;
    });
  }

  //2. Get Objects of a specific bucket
  objects: any[] = [];
  selectedBucket: string = '';

  loadObjects(bucketName: string) {
    this.selectedBucket = bucketName;
    this.s3.getBucketObjects(bucketName).subscribe(data => {
      this.objects = data;
    });
  }

}
