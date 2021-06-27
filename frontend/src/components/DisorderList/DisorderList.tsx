import React from 'react';
import { DisorderListProps } from './DisorderList.props';
import { observer } from 'mobx-react-lite';
import { Grid } from '@material-ui/core';
import { useMst } from '../../mobx/Root.store';
import { DisorderCard } from '../DisorderCard/DisorderCard';

export const DisorderList: React.FC<DisorderListProps> = observer(() => {
  const { lookupStore } = useMst();
  const { disorders, selectedHpoIds } = lookupStore;

  return (
    <Grid container spacing={1} direction="row">
      {disorders.slice().map(disorder => (
        <Grid item xs={12} md={4} key={disorder.id}>
          <DisorderCard disorder={disorder} selectedHpoIds={selectedHpoIds} />
        </Grid>
      ))}
    </Grid>
  );
});
