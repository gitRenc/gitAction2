import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { SimpleModule } from './simple/simple.module';
import { CronModule } from './cron/cron.module';

@Module({
  imports: [SimpleModule, CronModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
