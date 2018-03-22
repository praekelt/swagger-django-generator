import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    NumberField,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

export const SiteRoleLabelsAggregatedList = props => (
    <List {...props} title="SiteRoleLabelsAggregated List">
        <Datagrid>
            <NumberField source="site_id" />
        </Datagrid>
    </List>
)

export const SiteRoleLabelsAggregatedShow = props => (
    <Show {...props} title="SiteRoleLabelsAggregated Show">
        <SimpleShowLayout>
            <NumberField source="site_id" />
        </SimpleShowLayout>
    </Show>
)

