import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    DataGrid,
    SimpleShowLayout,
    SimpleForm,
    NumberField,
    TextField,
} from 'admin-on-rest';

export const PetList = props => (
    <List {...props} title={"Pet List"}>
        <DataGrid>
            <NumberField source="id" />
            <TextField source="status" />
            <TextField source="photoUrls" />
            <TextField source="name" />
        </DataGrid>
    </List>
)

export const PetShow = props => (
    <Show {...props} title={"Pet Show"}>
        <SimpleShowLayout>
            <NumberField source="id" />
            <TextField source="status" />
            <TextField source="photoUrls" />
            <TextField source="name" />
        </SimpleShowLayout>
    </Show>
)

