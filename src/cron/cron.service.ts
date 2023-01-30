import { Injectable } from '@nestjs/common';
import { Cron } from '@nestjs/schedule';
import { Octokit } from 'octokit';

@Injectable()
export class CronService {
  @Cron('0 02 15 * * 0-6', {
    name: 'Scheduler',
    timeZone: 'Asia/Makassar',
  })
  async handleCron() {
    const octokit = new Octokit({
      auth: `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 `,
    });

    // DATA INFO
    // owner        : git repo owner
    // repo         : git repo
    // workflow_id  : workflow filename in .github/workflow
    // ref          : branch
    //
    const response = await octokit.request(
      'POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches',
      {
        owner: 'gitRenc',
        repo: 'gitAction2',
        workflow_id: 'test.yml',
        ref: 'main',
      },
    );

    // should be return 204
    console.log(response.status);
  }
}
