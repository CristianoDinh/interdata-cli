import { Injectable } from '@angular/core';
import {S3Object} from '../interface/S3Object';

@Injectable({
  providedIn: 'root'
})
export class SampleService {
  constructor() { }

  protected bucketObjectList: S3Object[] =[
    //example json data
    {
      "id": 1,
      "name": "objectA",
      "last_modified": new Date("2025-02-25")
    },
    {
      "id": 2,
      "name": "objectB",
      "last_modified": new Date("2025-02-26")
    },
    {
      "id": 3,
      "name": "objectC",
      "last_modified": new Date("2025-02-27")
    },
    // có thể thay thế bước tạo dữ liệu mẫu trên bằng Factory Design Pattern
  ]

  getAllBucketObjects() : S3Object[] {
    return this.bucketObjectList;
  }
}
