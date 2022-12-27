/// <reference types="chrome"/>
import { Component, Input } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule } from '@angular/material/button';
import { NgCircleProgressModule } from 'ng-circle-progress';
import { VideosService } from '../videos.service'


@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.sass']
})
export class MainComponent {
  
  sentimentValue = 0;
  hideResults = true;

  constructor(private videoService:VideosService){
   
  }

  async onClick(event?: MouseEvent) {
    const evtMsg = event ? ' Event target class is ' + (event.target as HTMLElement).className  : '';
    this.hideResults = false;
    
    let queryOptions = { active: true, currentWindow: true };
    let [tab] = await chrome.tabs.query(queryOptions);
    if(!!tab){
      let videoId = tab.url ? tab.url.split("=")[1] : ""
      console.log(tab.url);
      this.videoService.getVideoSentiment(videoId).subscribe((data: any) => {
        console.log("DATA: " + JSON.stringify(data));
        console.log(window.location.href)
        
        this.sentimentValue = Math.round(((data["avgSentiment"] + 1)/2)*100)
      })
    } else {
      console.log("cannot produce results")
    }
    
  }

  
  
}
