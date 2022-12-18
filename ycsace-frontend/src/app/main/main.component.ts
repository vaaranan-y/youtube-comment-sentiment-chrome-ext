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
  
  sentimentValue = 20;
  constructor(private video:VideosService){
    this.video.getVideoSentiment().subscribe((data: any) => {
      console.log("DATA: " + JSON.stringify(data));
      this.sentimentValue = Math.round(((data["avgSentiment"] + 1)/2)*100)
    })
  }
  
}
