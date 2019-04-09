import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Routes, RouterModule } from '@angular/router';

import { IonicModule } from '@ionic/angular';

import { ScannerPage } from './scanner.page';
import { ComponentsModule } from '../../components/components.module';
// import { Camera, CameraOptions } from '@ionic-native/camera';

const routes: Routes = [
  {
    path: '',
    component: ScannerPage
  }
];

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    RouterModule.forChild(routes),
    ComponentsModule
  ],
  declarations: [ScannerPage]
})
export class ScannerPageModule {
  // constructor(private camera: Camera) {}
}
