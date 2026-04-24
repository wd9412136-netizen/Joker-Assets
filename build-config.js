// Capacitor Build Configuration
const fs = require('fs');
const path = require('path');

module.exports = {
  // App Configuration
  appId: 'com.jokerapp.mobile',
  appName: 'الجوكر',
  package: 'com.jokerapp.mobile',
  
  // Android Configuration
  android: {
    minSdkVersion: 21,
    targetSdkVersion: 33,
    compileSdkVersion: 33,
    gradleVersion: '7.0',
    buildToolsVersion: '33.0.0'
  },
  
  // App Icons and Splash
  icons: {
    android: {
      ldpi: 36,
      mdpi: 48,
      hdpi: 72,
      xhdpi: 96,
      xxhdpi: 144,
      xxxhdpi: 192
    }
  }
};
