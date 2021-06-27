import { getRoot, IStateTreeNode } from 'mobx-state-tree';

export const withRoot = (self: IStateTreeNode) => ({
  views: {
    get root() {
      return getRoot(self) as any;
    },
  },
});
