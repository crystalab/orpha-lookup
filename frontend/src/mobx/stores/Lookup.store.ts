import { flow, types } from 'mobx-state-tree';
import { Hpo } from '../models/Hpo';
import { withApi } from '../extensions/withApi';
import { withRoot } from '../extensions/withRoot';
import { Disorder } from '../models/Disorder';

export const LookupStore = types.model({
  suggestionsLoading: false,
  suggestions: types.optional(types.array(types.reference(Hpo)), []),

  selectedHpos: types.optional(types.array(types.reference(Hpo)), []),

  disordersLoading: false,
  disorders: types.optional(types.array(types.reference(Disorder)), []),
})
  .extend(withApi)
  .extend(withRoot)
  .views(self => ({
    get selectedHpoIds() {
      return self.selectedHpos.reduce((acc: any, hpo) => {
        acc[hpo.id] = true;
        return acc;
      }, {});
    },
  }))
  .actions(self => ({
    loadSuggestions: flow(function *(searchText: string) {
      self.suggestionsLoading = true;
      try {
        const response = yield self.api.get('/hpos/', { search: searchText });
        self.suggestions = self.root.repoStore.persistHpoResponse(response.data);
      } finally {
        self.suggestionsLoading = false;
      }
    }),
    loadDisorders: flow(function *() {
      self.disordersLoading = true;
      try {
        const ids = Object.keys(self.selectedHpoIds).join(',');
        const response = yield self.api.get('/disorders/', { hpo: ids });
        self.disorders = self.root.repoStore.persistDisordersResponse(response.data);
      } finally {
        self.disordersLoading = false;
      }
    }),
  }))
  .actions(self => ({
    searchFor(text: string) {
      self.loadSuggestions(text);
    },
    setHpos(hpos: any) {
      self.selectedHpos = hpos;
      self.loadSuggestions('');
      self.loadDisorders();
    },
  }));
