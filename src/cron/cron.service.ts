import { Injectable } from '@nestjs/common';
import { Cron } from '@nestjs/schedule';

@Injectable()
export class CronService {
  @Cron('0 49 14 * * 0-6', {
    name: 'Scheduler',
    timeZone: 'Asia/Makassar',
  })
  handleCron() {
    console.log('yup');
  }
}
