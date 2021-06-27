import { ApisauceInstance, create } from 'apisauce';
import { camelizeKeys, decamelizeKeys } from 'humps';

export class Api {
  public client: ApisauceInstance;

  constructor(apiUrl: string) {
    this.client = create({
      baseURL: apiUrl,
    });

    this.client.addRequestTransform(request => {
      request.withCredentials = true;
      request.data = decamelizeKeys(request.data);
      request.params = decamelizeKeys(request.params);
    });

    this.client.addResponseTransform(response => {
      response.data = camelizeKeys(response.data);
    });
  }
}
