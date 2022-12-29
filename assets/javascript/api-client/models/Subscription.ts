/* tslint:disable */
/* eslint-disable */
/**
 * QuicDoc
 * Software meant to save you time editing documents and allow you to spend more time bringing in customers
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { exists, mapValues } from '../runtime';
import type { StatusEnum } from './StatusEnum';
import {
    StatusEnumFromJSON,
    StatusEnumFromJSONTyped,
    StatusEnumToJSON,
} from './StatusEnum';
import type { SubscriptionItem } from './SubscriptionItem';
import {
    SubscriptionItemFromJSON,
    SubscriptionItemFromJSONTyped,
    SubscriptionItemToJSON,
} from './SubscriptionItem';

/**
 * A serializer for Subscriptions which uses the SubscriptionWrapper object under the hood
 * @export
 * @interface Subscription
 */
export interface Subscription {
    /**
     * 
     * @type {string}
     * @memberof Subscription
     */
    id: string;
    /**
     * 
     * @type {string}
     * @memberof Subscription
     */
    displayName: string;
    /**
     * Date when the subscription was first created. The date might differ from the created date due to backdating.
     * @type {Date}
     * @memberof Subscription
     */
    startDate?: Date | null;
    /**
     * 
     * @type {string}
     * @memberof Subscription
     */
    billingInterval: string;
    /**
     * Start of the current period for which the subscription has been invoiced.
     * @type {Date}
     * @memberof Subscription
     */
    currentPeriodStart: Date;
    /**
     * End of the current period for which the subscription has been invoiced. At the end of this period, a new invoice will be created.
     * @type {Date}
     * @memberof Subscription
     */
    currentPeriodEnd: Date;
    /**
     * If the subscription has been canceled with the ``at_period_end`` flag set to true, ``cancel_at_period_end`` on the subscription will be true. You can use this attribute to determine whether a subscription that has a status of active is scheduled to be canceled at the end of the current period.
     * @type {boolean}
     * @memberof Subscription
     */
    cancelAtPeriodEnd?: boolean;
    /**
     * The status of this subscription.
     * @type {StatusEnum}
     * @memberof Subscription
     */
    status: StatusEnum;
    /**
     * The quantity applied to this subscription. This value will be `null` for multi-plan subscriptions
     * @type {number}
     * @memberof Subscription
     */
    quantity?: number | null;
    /**
     * 
     * @type {Array<SubscriptionItem>}
     * @memberof Subscription
     */
    items: Array<SubscriptionItem>;
}

/**
 * Check if a given object implements the Subscription interface.
 */
export function instanceOfSubscription(value: object): boolean {
    let isInstance = true;
    isInstance = isInstance && "id" in value;
    isInstance = isInstance && "displayName" in value;
    isInstance = isInstance && "billingInterval" in value;
    isInstance = isInstance && "currentPeriodStart" in value;
    isInstance = isInstance && "currentPeriodEnd" in value;
    isInstance = isInstance && "status" in value;
    isInstance = isInstance && "items" in value;

    return isInstance;
}

export function SubscriptionFromJSON(json: any): Subscription {
    return SubscriptionFromJSONTyped(json, false);
}

export function SubscriptionFromJSONTyped(json: any, ignoreDiscriminator: boolean): Subscription {
    if ((json === undefined) || (json === null)) {
        return json;
    }
    return {
        
        'id': json['id'],
        'displayName': json['display_name'],
        'startDate': !exists(json, 'start_date') ? undefined : (json['start_date'] === null ? null : new Date(json['start_date'])),
        'billingInterval': json['billing_interval'],
        'currentPeriodStart': (new Date(json['current_period_start'])),
        'currentPeriodEnd': (new Date(json['current_period_end'])),
        'cancelAtPeriodEnd': !exists(json, 'cancel_at_period_end') ? undefined : json['cancel_at_period_end'],
        'status': StatusEnumFromJSON(json['status']),
        'quantity': !exists(json, 'quantity') ? undefined : json['quantity'],
        'items': ((json['items'] as Array<any>).map(SubscriptionItemFromJSON)),
    };
}

export function SubscriptionToJSON(value?: Subscription | null): any {
    if (value === undefined) {
        return undefined;
    }
    if (value === null) {
        return null;
    }
    return {
        
        'id': value.id,
        'display_name': value.displayName,
        'start_date': value.startDate === undefined ? undefined : (value.startDate === null ? null : value.startDate.toISOString()),
        'billing_interval': value.billingInterval,
        'current_period_start': (value.currentPeriodStart.toISOString()),
        'current_period_end': (value.currentPeriodEnd.toISOString()),
        'cancel_at_period_end': value.cancelAtPeriodEnd,
        'status': StatusEnumToJSON(value.status),
        'quantity': value.quantity,
        'items': ((value.items as Array<any>).map(SubscriptionItemToJSON)),
    };
}

