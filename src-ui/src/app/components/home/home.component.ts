import {AfterViewInit, Component, ElementRef, inject, OnInit, ViewChild} from '@angular/core';
import {S3Object} from '../../interface/S3Object';
import {SampleService} from '../../services/sample.service';
import {NgForOf} from '@angular/common';
import {BucketObjectComponent} from '../bucket-object/bucket-object.component';
import {FormsModule} from '@angular/forms';
import {S3Service} from '../../services/s3.service';
import {Observable} from 'rxjs';
import {S3Bucket} from '../../interface/S3Bucket';


@Component({
  selector: 'app-home',
  imports: [
    BucketObjectComponent,
    FormsModule,
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements AfterViewInit, OnInit {
  s3Service: S3Service = inject(S3Service);

//(1). Get buckets
  bucketList !: S3Bucket[];
  ngOnInit() {
    this.s3Service.getBuckets().subscribe(data => {
      this.bucketList = data;
    })
  }
  @ViewChild('searchInput') searchInput!: ElementRef;
  ngAfterViewInit() {
    this.searchInput.nativeElement.focus(); // Đặt con trỏ vào ô input khi component tải xong
  }
  searchTerm !: string;

//(2). Get objects of a specific bucket
  bucketObjectList: S3Object[] = [];

  constructor() {
    this.s3Service.getBucketObjects("s3-2427-27838-storage-default").subscribe(data => {
      this.bucketObjectList = data;
    })
    console.log(this.bucketObjectList)
  }

}
