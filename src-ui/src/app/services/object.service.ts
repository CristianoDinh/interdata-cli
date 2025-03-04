import { Injectable } from '@angular/core';
import {BucketObject} from '../interface/bucketObject';

@Injectable({
  providedIn: 'root'
})
export class ObjectService {
  constructor() { }

  protected bucketObjectList: BucketObject[] =[
    //example json data
    {
      "id": 1,
      "name": "objectA",
      "modifiedDate": new Date("2025-02-29")
    },
    {
      "id": 2,
      "name": "objectB",
      "modifiedDate": new Date("2025-02-30")
    },
    {
      "id": 3,
      "name": "objectC",
      "modifiedDate": new Date("2025-02-31")
    },
  ]
// có thể thay thế bước tạo dữ liệu mẫu trên bằng Factory Design Pattern

  getAllBucketObjects() : BucketObject[] {
    return this.bucketObjectList;
  }



}
