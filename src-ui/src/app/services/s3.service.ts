import {inject, Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
  providedIn: 'root'
})


export class S3Service {
  private apiUrl = 'http://127.0.0.1:5000';
  //Phiên bản Angular 14 trở về trước:  constructor( private http: HttpClient ) { }
  http = inject(HttpClient);

  //1. Gọi API get List buckets
  getBuckets(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/buckets`);
  }

  //2. Gọi API get list objects IN bucket
  getBucketObjects(bucketName: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/buckets/${bucketName}/objects`);
  }

}
