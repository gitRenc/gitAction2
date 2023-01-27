import { Controller, Get } from '@nestjs/common';

@Controller('cron')
export class CronController {
  @Get()
  test(): string {
    return 'jing';
  }
}
