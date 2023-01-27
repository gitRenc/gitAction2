import { Controller, Get } from '@nestjs/common';

@Controller('simple')
export class SimpleController {
  @Get()
  test(): string {
    return 'Scheduling your Github Action Workflow!';
  }
}
