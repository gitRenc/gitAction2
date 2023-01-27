import { Injectable } from '@nestjs/common';
import { Cron } from '@nestjs/schedule';

@Injectable()
export class CronService {
  @Cron('0 02 15 * * 0-6', {
    name: 'Scheduler',
    timeZone: 'Asia/Makassar',
  })
  handleCron() {
    console.log('yup2');
  }
}
