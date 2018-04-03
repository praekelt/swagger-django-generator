/**
 * Generated SiteRole.js code. Edit at own risk.
 * When regenerated the changes will be lost.
**/
import React from 'react';
import {
    List,
    Datagrid,
    ReferenceField,
    NumberField,
    BooleanField,
    DateField,
    SimpleForm,
    Create,
    ReferenceInput,
    SelectInput,
    BooleanInput,
    Show,
    SimpleShowLayout,
    Edit,
    DisabledInput,
    DeleteButton,
    EditButton,
    ShowButton
} from 'admin-on-rest';
import {
    SiteRoleFilter
} from './Filters';

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

export const SiteRoleList = props => (
    <List {...props} title="SiteRole List" filters={<SiteRoleFilter />}>
        <Datagrid>
            <ReferenceField label="Site" source="site_id" reference="sites" linkType="show" allowEmpty>
                <NumberField source="name" />
            </ReferenceField>
            <ReferenceField label="Role" source="role_id" reference="roles" linkType="show" allowEmpty>
                <NumberField source="label" />
            </ReferenceField>
            <BooleanField source="grant_implicitly" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
            <EditButton />
            <ShowButton />
            <DeleteButton />
        </Datagrid>
    </List>
)

export const SiteRoleCreate = props => (
    <Create {...props} title="SiteRole Create">
        <SimpleForm validate={validationCreateSiteRole}>
            <ReferenceInput label="Site" source="site_id" reference="sites" allowEmpty>
                <SelectInput source="id" optionText="name" />
            </ReferenceInput>
            <ReferenceInput label="Role" source="role_id" reference="roles" allowEmpty>
                <SelectInput source="id" optionText="label" />
            </ReferenceInput>
            <BooleanInput source="grant_implicitly" />
        </SimpleForm>
    </Create>
)

export const SiteRoleShow = props => (
    <Show {...props} title="SiteRole Show">
        <SimpleShowLayout>
            <ReferenceField label="Site" source="site_id" reference="sites" linkType="show" allowEmpty>
                <NumberField source="name" />
            </ReferenceField>
            <ReferenceField label="Role" source="role_id" reference="roles" linkType="show" allowEmpty>
                <NumberField source="label" />
            </ReferenceField>
            <BooleanField source="grant_implicitly" />
            <DateField source="created_at" />
            <DateField source="updated_at" />
        </SimpleShowLayout>
    </Show>
)

export const SiteRoleEdit = props => (
    <Edit {...props} title="SiteRole Edit">
        <SimpleForm validate={validationEditSiteRole}>
            <BooleanInput source="grant_implicitly" />
        </SimpleForm>
    </Edit>
)

/** End of Generated Code **/