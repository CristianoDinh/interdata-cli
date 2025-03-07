import {AfterViewInit, Component, ElementRef, inject, ViewChild} from '@angular/core';
import {S3Object} from '../../interface/S3Object';
import {SampleService} from '../../services/sample.service';
import {NgForOf} from '@angular/common';
import {BucketObjectComponent} from '../bucket-object/bucket-object.component';
import {FormsModule} from '@angular/forms';


@Component({
  selector: 'app-home',
  imports: [
    BucketObjectComponent,
    FormsModule,
  ],
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent implements AfterViewInit {
  @ViewChild('searchInput') searchInput!: ElementRef;
  ngAfterViewInit() {
    this.searchInput.nativeElement.focus(); // Đặt con trỏ vào ô input khi component tải xong
  }

  bucketObjectList: S3Object[] = [];
  sampleService: SampleService = inject(SampleService);
  searchTerm !: string;

  constructor() {
    this.bucketObjectList = this.sampleService.getAllBucketObjects();
  }


}
