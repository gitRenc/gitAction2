import { Test, TestingModule } from '@nestjs/testing';
import { SimpleController } from './simple.controller';

describe('SimpleController', () => {
  let controller: SimpleController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [SimpleController],
    }).compile();

    controller = module.get<SimpleController>(SimpleController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
