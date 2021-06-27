import { getEnv, IStateTreeNode } from 'mobx-state-tree';
import { Environment } from '../Environment';

export const withApi = (self: IStateTreeNode) => ({
  views: {
    get api() {
      return getEnv<Environment>(self).api.client;
    },
  },
});
