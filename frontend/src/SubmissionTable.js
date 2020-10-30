import React from 'react';
import { DataGrid } from '@material-ui/data-grid';

const columns = [
  {field: 'id', headerName: 'ID'},
  {
    field: 'status',
    headerName: 'Status',
    sortable: false,
    width: 75,
    valueGetter: (params) => 
      params.getValue('status') === 'IN_PROGRESS' ? `⏳` : params.getValue('index') && params.getValue('index') >= 0 ? `✅` : `❌`
  },
  {field: 'query', headerName: 'Query', width:250},
  {field: 'name', headerName: 'Match', width: 150},
  {field: 'index', headerName: 'Index'},
  {field: 'description', headerName: 'Description', width:250},
  {field: 'protein', headerName: 'Protein', width:150},
];

function SubmissionTable({
  submissions
}) {
  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid rows={submissions} columns={columns} pageSize={10} />
    </div>
  );
}

export default SubmissionTable;