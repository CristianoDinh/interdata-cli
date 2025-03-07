import {Component, inject, OnInit} from '@angular/core';
import {S3Service} from '../services/s3.service';
import {NgForOf, NgIf} from '@angular/common';
import {S3Bucket} from '../interface/S3Bucket';
import {S3Object} from '../interface/S3Object';

@Component({
  selector: 'app-test-api',
  imports: [
    NgForOf
  ],
  templateUrl: './test-api.component.html',
  styleUrl: './test-api.component.css'
})
export class TestAPIComponent implements OnInit {
  // Danh sách buckets
  buckets: S3Bucket[] = [];
  objectsMap: { [key: string]: S3Object[] } = {};  // Lưu objects theo từng bucket
  s3 = inject(S3Service);

  ngOnInit() {
    this.s3.getBuckets().subscribe(buckets => {
      this.buckets = buckets;

      // Gọi API lấy objects cho từng bucket ngay sau khi có danh sách buckets
      this.buckets.forEach(bucket => {
        this.s3.getBucketObjects(bucket.name).subscribe(objects => {
          this.objectsMap[bucket.name] = objects;
        });
      });
    });
  }
}
