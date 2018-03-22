import React from 'react';
import {
    List,
    Show,
    Edit,
    Create,
    Datagrid,
    SimpleShowLayout,
    SimpleForm,
    DateField,
    DateInput,
    NumberField,
    NumberInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateSiteDataSchema = values => {
    const errors = {};
    if (!values.site_id) {
        errors.site_id = ["site_id is required"];
    }
    return errors;
}

const validationEditSiteDataSchema = values => {
    const errors = {};
    return errors;
}

export const SiteDataSchemaList = props => (
    <List {...props} title="SiteDataSchema List">
        <Datagrid>
            <DateField source="updated_at" />
            <NumberField source="site_id" />
            <DateField source="created_at" />
            <EditButton />
        </Datagrid>
    </List>
)

export const SiteDataSchemaShow = props => (
    <Show {...props} title="SiteDataSchema Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <NumberField source="site_id" />
            <DateField source="created_at" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const SiteDataSchemaCreate = props => (
    <Create {...props} title="Create SiteDataSchema">
        <SimpleForm validate={validationCreateSiteDataSchema}>
            <NumberInput source="site_id" />
        </SimpleForm>
    </Create>
)

export const SiteDataSchemaEdit = props => (
    <Edit {...props} title="Edit SiteDataSchema">
        <SimpleForm validate={validationEditSiteDataSchema}>
        </SimpleForm>
    </Edit>
)

