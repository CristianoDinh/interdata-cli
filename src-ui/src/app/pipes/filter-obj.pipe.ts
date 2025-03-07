import { Pipe, PipeTransform } from '@angular/core';
import {S3Object} from '../interface/S3Object';

@Pipe({
  name: 'filterObj'
})
export class FilterObjPipe implements PipeTransform {

  transform(objects: S3Object[], searchTerm: string): S3Object[] {
    if(!searchTerm) {
      return objects;
    }
    const text= searchTerm.toLowerCase();
    return objects.filter(obj => {
      return obj.name.toLowerCase().includes(text);
    })
  }

}
