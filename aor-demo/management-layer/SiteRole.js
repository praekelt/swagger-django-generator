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
    BooleanField,
    BooleanInput,
    DisabledInput,
    EditButton

} from 'admin-on-rest';

const validationCreateSiteRole = values => {
    const errors = {};
    if (!values.role_id) {
        errors.role_id = ["role_id is required"];
    }
    if (!values.site_id) {
        errors.site_id = ["site_id is required"];
    }
    return errors;
}

const validationEditSiteRole = values => {
    const errors = {};
    return errors;
}

export const SiteRoleList = props => (
    <List {...props} title="SiteRole List">
        <Datagrid>
            <DateField source="updated_at" />
            <NumberField source="role_id" />
            <BooleanField source="grant_implicitly" />
            <DateField source="created_at" />
            <NumberField source="site_id" />
            <EditButton />
        </Datagrid>
    </List>
)

export const SiteRoleShow = props => (
    <Show {...props} title="SiteRole Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <NumberField source="role_id" />
            <BooleanField source="grant_implicitly" />
            <DateField source="created_at" />
            <NumberField source="site_id" />
            <EditButton />
        </SimpleShowLayout>
    </Show>
)

export const SiteRoleCreate = props => (
    <Create {...props} title="Create SiteRole">
        <SimpleForm validate={validationCreateSiteRole}>
            <NumberInput source="role_id" />
            <BooleanInput source="grant_implicitly" />
            <NumberInput source="site_id" />
        </SimpleForm>
    </Create>
)

export const SiteRoleEdit = props => (
    <Edit {...props} title="Edit SiteRole">
        <SimpleForm validate={validationEditSiteRole}>
            <BooleanInput source="grant_implicitly" />
        </SimpleForm>
    </Edit>
)

