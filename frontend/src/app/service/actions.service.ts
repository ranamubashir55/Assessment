
import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { catchError } from 'rxjs/operators';
import { throwError, Observable, of } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class ActionsService {
  private baseApiUrl = 'http://127.0.0.1:8080';
   base_url = this.baseApiUrl;

  constructor( private _http: HttpClient) { }
  //  stats() {
  //   return this._http.get<any>(this.base_url + '/get_file_usage')
  //   .pipe(catchError(this.errorHandler));
  //   // var data = [{'status': 'healthy', 'memory': '450MB', 'Drive': 'samsumg'}];
  //   // return data;
  //  }

   stats(data: any) {
    return this._http.post<any>(this.base_url + '/get_file_usage', data)
    .pipe(catchError(this.errorHandler));
   }
  private errorHandler( error: HttpErrorResponse) {
    return throwError(error);
  }

}
