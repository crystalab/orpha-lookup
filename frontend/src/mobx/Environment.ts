import { Api } from '../services/Api';

export class Environment {
  api: Api;

  constructor(apiUrl: string) {
    this.api = new Api(apiUrl);
  }
}
