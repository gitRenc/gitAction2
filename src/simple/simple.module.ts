import { Module } from '@nestjs/common';
import { SimpleController } from './simple.controller';

@Module({
  imports: [],
  controllers: [SimpleController],
  providers: [],
})
export class SimpleModule {}
