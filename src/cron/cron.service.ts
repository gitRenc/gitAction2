import { Injectable } from '@nestjs/common';
import { Cron } from '@nestjs/schedule';

@Injectable()
export class CronService {
  @Cron('*/5 59 0 * * 0-6')
  handleCron() {
    console.log('oke');
  }
}
