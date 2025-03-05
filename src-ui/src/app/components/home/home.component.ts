import {AfterViewInit, Component, ElementRef, inject, ViewChild} from '@angular/core';
import {BucketObject} from '../../interface/bucketObject';
import {ObjectService} from '../../services/object.service';
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

  bucketObjectList: BucketObject[] = [];
  objectService: ObjectService = inject(ObjectService);
  searchTerm !: string;

  constructor() {
    this.bucketObjectList = this.objectService.getAllBucketObjects();
  }


}
