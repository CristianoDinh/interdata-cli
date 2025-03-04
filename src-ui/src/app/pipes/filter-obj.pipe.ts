import { Pipe, PipeTransform } from '@angular/core';
import {BucketObject} from '../interface/bucketObject';

@Pipe({
  name: 'filterObj'
})
export class FilterObjPipe implements PipeTransform {

  transform(objects: BucketObject[], searchTerm: string): BucketObject[] {
    if(!searchTerm) {
      return objects;
    }
    const text= searchTerm.toLowerCase();
    return objects.filter(obj => {
      return obj.name.toLowerCase().includes(text);
    })
  }

}
