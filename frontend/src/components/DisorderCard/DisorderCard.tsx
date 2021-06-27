import React from 'react';
import { DisorderCardProps } from './DisorderCard.props';
import { observer } from 'mobx-react-lite';
import { Box, Button, Card, CardActions, CardContent, Chip, Grid, Typography } from '@material-ui/core';
import { ExpandLess, ExpandMore } from '@material-ui/icons';

export const DisorderCard: React.FC<DisorderCardProps> = observer(props => {
  const { disorder, selectedHpoIds } = props;
  const [expanded, setExpanded] = React.useState(false);

  const sortedHpos = disorder.sortedHpos(selectedHpoIds);
  const sortedHpoChunk = expanded ? sortedHpos : sortedHpos.slice(0, 5);

  return (
    <Card>
      <CardContent>
        <Typography variant="h5" gutterBottom>
          {disorder.name}
          {disorder.disorderGroup && (
            <Chip color="secondary" variant="outlined" label={disorder.disorderGroup} size="small" />
          )}

          {disorder.disorderType && (
            <Chip color="secondary" variant="outlined" label={disorder.disorderType} size="small" />
          )}
        </Typography>

        <Box>
          <Grid container direction="row" justify="space-between">
            <Typography variant="h6">
              Symptoms
            </Typography>
            {sortedHpos.length > 5 && (
              <>
                {expanded && (
                  <Button size="small" onClick={() => setExpanded(false)}>
                    <ExpandLess />
                    Show less
                  </Button>
                )}
                {!expanded && (
                  <Button size="small" onClick={() => setExpanded(true)}>
                    <ExpandMore />
                    Show all {sortedHpos.length}
                  </Button>
                )}
              </>
            )}


          </Grid>

          {sortedHpoChunk.map(disorderHpo => {
            const hpo = disorderHpo.hpo;
            return (
              <Chip
                variant={hpo.id in selectedHpoIds ? 'default' : 'outlined'}
                color={hpo.id in selectedHpoIds ? 'primary' : 'default'}
                label={hpo.name}
                size="small" />
            );
          })}
        </Box>

      </CardContent>
      <CardActions>
        {disorder.expertLink && (
          <Button size="small" target="_blank" href={disorder.expertLink}>Learn More</Button>
        )}
      </CardActions>
    </Card>
  );
});
