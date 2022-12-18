import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class VideosService {
  rootURL = "http://127.0.0.1:8000";

  constructor(private http:HttpClient) { }

  getVideoSentiment(){
    let url = this.rootURL + '/sentiment-analyzer/get-video-sentiment/nWiQodhMvz4';
    return this.http.get(url);

  }
}
