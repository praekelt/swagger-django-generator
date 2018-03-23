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
    NumberField,
    BooleanField,
    BooleanInput,
    NumberInput,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';

const validationCreateSiteRole = values => {
    const errors = {};
    if (!values.site_id) {
        errors.site_id = ["site_id is required"];
    }
    if (!values.role_id) {
        errors.role_id = ["role_id is required"];
    }
    return errors;
}

const validationEditSiteRole = values => {
    const errors = {};
    return errors;
}

export const SiteRoleShow = props => (
    <Show {...props} title="SiteRole Show">
        <SimpleShowLayout>
            <DateField source="updated_at" />
            <ReferenceField label="Role" source="role_id" reference="roles" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <BooleanField source="grant_implicitly" />
            <ReferenceField label="Site" source="site_id" reference="sites" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <DateField source="created_at" />
        </SimpleShowLayout>
    </Show>
)

export const SiteRoleEdit = props => (
    <Edit {...props} title="SiteRole Edit">
        <SimpleForm validate={validationCreateSiteRole}>
            <BooleanInput source="grant_implicitly" />
        </SimpleForm>
    </Edit>
)

export const SiteRoleCreate = props => (
    <Create {...props} title="SiteRole Create">
        <SimpleForm validate={validationCreateSiteRole}>
            <BooleanInput source="grant_implicitly" />
            <ReferenceInput label="Site" source="site_id" reference="sites" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
            <ReferenceInput label="Role" source="role_id" reference="roles" allowEmpty>
                <SelectInput source="id" />
            </ReferenceInput>
        </SimpleForm>
    </Create>
)

export const SiteRoleList = props => (
    <List {...props} title="SiteRole List">
        <Datagrid>
            <DateField source="updated_at" />
            <ReferenceField label="Role" source="role_id" reference="roles" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <BooleanField source="grant_implicitly" />
            <ReferenceField label="Site" source="site_id" reference="sites" allowEmpty>
                <NumberField source="id" />
            </ReferenceField>
            <DateField source="created_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

